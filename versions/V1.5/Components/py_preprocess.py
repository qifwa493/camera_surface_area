# -*- coding: utf-8 -*-

import cv2
import numpy as np
import pickle


def addSoftBorder(Image, BorderPix):
    # This function adds a soft black border to the image

    # Create a mask with the size of the original image
    size = Image.shape[:2]
    mask = np.zeros([size[0], size[1]], dtype=np.uint8)
    mask = cv2.rectangle(mask, (BorderPix, BorderPix), (size[1] - BorderPix, size[0] - BorderPix), 255, -1)

    # Create a gradient at the border
    mask = cv2.blur(mask, (21, 21))
    mask = cv2.merge((mask, mask, mask)) / 255

    # Apply the mask to the image and return the outcome
    return cv2.convertScaleAbs(Image * mask)


def undistortImage(Image, CameraMatrix, StoreImage=False, ImageName='Image'):
    # Get the parameters
    with open(CameraMatrix, 'rb') as f:
        cameraMatrix = pickle.load(f)
        mtx = cameraMatrix['mtx']
        dist = cameraMatrix['dist']

    # Undistort
    dst = cv2.undistort(Image, mtx, dist, None, mtx)

    # Store the undistorted image
    if StoreImage:
        cv2.imwrite(ImageName + '_undistorted.jpg', dst)

    return dst


def findChessboardInImage(Image, Width=6, Height=9):
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (Height, Width), None)

    # If found, return corners
    if ret:
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        return corners2
    else:
        return []


def getChessboardCorners(Corners, Width=6, Height=9):
    # Get the 4 corner points of the chessboard
    points = Corners[0]
    for i in (Height - 1, (Width - 1) * Height, Width * Height - 1):
        # points = np.vstack((points, Corners[i]))
        points = np.vstack((Corners[i], points))
    return points


def getNewPoints(Width=6, Height=9, Size=(8000, 8000), Direction=1):
    # Get the 4 new points based on the chessboard size

    halfWidth = (Height - 1) * 50
    halfHeight = (Width - 1) * 50

    if Direction == 1:
        p1 = np.float32([Size[0] / 2 - halfWidth, Size[1] / 2 - halfHeight])
        p2 = np.float32([Size[0] / 2 + halfWidth, Size[1] / 2 - halfHeight])
        p3 = np.float32([Size[0] / 2 - halfWidth, Size[1] / 2 + halfHeight])
        p4 = np.float32([Size[0] / 2 + halfWidth, Size[1] / 2 + halfHeight])
    else:
        p1 = np.float32([Size[0] / 2 - halfHeight, Size[1] / 2 + halfWidth])
        p2 = np.float32([Size[0] / 2 - halfHeight, Size[1] / 2 - halfWidth])
        p3 = np.float32([Size[0] / 2 + halfHeight, Size[1] / 2 + halfWidth])
        p4 = np.float32([Size[0] / 2 + halfHeight, Size[1] / 2 - halfWidth])

    return np.vstack((p1, p2, p3, p4))


def cropImgPerspectively(Image, OldPoints, NewPoints, Size=(8000, 8000)):
    # From the Old and New points get the transform matrix, then crop image

    # showImg('before transform', Image, 800)
    # cv2.waitKey(0)
    # cv2.destroyWindow('before transform')
    M = cv2.getPerspectiveTransform(OldPoints, NewPoints)
    return cv2.warpPerspective(Image, M, Size)


def showImg(winName, mat, Width=None, Height=None):
    # Get image size
    # if Width is None or Height is None:
    #     Height, Width = mat.shape[:2]

    dim = None

    # if both the width and height are None
    if Width is None and Height is None:
        dim = mat.shape[:2]

    # check to see if the width is None
    elif Width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = Height / float(mat.shape[0])
        dim = (int(mat.shape[1] * r), Height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = Width / float(mat.shape[1])
        dim = (Width, int(mat.shape[0] * r))

    # Display image
    cv2.namedWindow(winName, 0)
    cv2.resizeWindow(winName, dim[0], dim[1])
    cv2.imshow(winName, mat)


def cropBlackBorder(Image):
    # This function crop the balck border of an image

    # Convert the image to gray
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    _, gray = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

    # Get bounding rectangle
    x, y, w, h = cv2.boundingRect(gray)
    return Image[y + 10:y + h - 10, x + 10:x + w - 10]


def reduceImgSize(Image, LongSide):
    imgSize = Image.shape[:2]
    if imgSize[0] < LongSide and imgSize[1] < LongSide:
        return Image

    if imgSize[0] > imgSize[1]:
        imgScale = LongSide / imgSize[0]
    else:
        imgScale = LongSide / imgSize[1]
    newX, newY = imgSize[1] * imgScale, imgSize[0] * imgScale
    return cv2.resize(Image, (int(newX), int(newY)))


if __name__ == '__main__':
    MainImage = cv2.imread('DSC_0631.JPG')
    showImg('Before', MainImage, 900)
    cv2.waitKey(1)
    MainImage = undistortImage(MainImage, 'matrix.p')
    corners = findChessboardInImage(MainImage, Width=6, Height=9)
    oldChessBoardCorners = getChessboardCorners(corners)
    ChessBoardCorners = getNewPoints(Width=6, Height=9, Size=(8000, 8000))

    # Transform and save the image
    MainImage = cropImgPerspectively(MainImage, oldChessBoardCorners, ChessBoardCorners)
    # cv2.imwrite('imgAfter', MainImage)
    showImg('After', MainImage, 900, 900)
    cv2.waitKey(1)

    # Crop the black border
    crop = cropBlackBorder(MainImage)
    showImg('crop', crop, 800)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
