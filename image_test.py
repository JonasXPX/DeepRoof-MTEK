import cv2 as cv

def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAI)


image = cv.imread('./images/temp.jpg')
# im = cv.equalize(image)
resized = cv.resize(image, (900, 600))

shifted = cv.pyrMeanShiftFiltering(resized, 12, 71)
gray = cv.cvtColor(shifted, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(gray, (7,7), 1)

thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]

cv.imshow('test', thresh)
cv.imshow('test2', resized)
cv.imshow('test3', imgBlur)
cv.waitKey(0)