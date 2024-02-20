import cv2

img = cv2.imread('solar-system.jpg')

cv2.putText(
  img,
  'Sun',
  (50 , 100),
  cv2.FONT_HERSHEY_COMPLEX,
  0.5,
  (255 , 255 , 255)
)

cv2.putText(
  img,
  'Mercury',
  (125 , 100),
  cv2.FONT_HERSHEY_COMPLEX,
  0.5,
  (255 , 255 , 255)
)

cv2.putText(
  img,
  'Venus',
  (195 , 120),
  cv2.FONT_HERSHEY_COMPLEX,
  0.5,
  (255 , 255 , 255)
)

cv2.putText(
  img,
  'Earth',
  (269 , 100),
  cv2.FONT_HERSHEY_COMPLEX,
  0.5,
  (255 , 255 , 255)
)

cv2.putText(
  img,
  'Mars',
  (375 , 140),
  cv2.FONT_HERSHEY_COMPLEX,
  0.5,
  (255 , 255 , 255)
)

cv2.putText(
  img,
  'Jupiter',
  (510 , 40),
  cv2.FONT_HERSHEY_COMPLEX,
  0.5,
  (255 , 255 , 255)
)

cv2.putText(
  img,
  'Saturn',
  (650 , 140),
  cv2.FONT_HERSHEY_COMPLEX,
  0.5,
  (255 , 255 , 255)
)

cv2.putText(
  img,
  'Uranus',
  (920 , 140),
  cv2.FONT_HERSHEY_COMPLEX,
  0.5,
  (255 , 255 , 255)
)

cv2.putText(
  img,
  'Neptune',
  (1099 , 140),
  cv2.FONT_HERSHEY_COMPLEX,
  0.5,
  (255 , 255 , 255)
)

cv2.imshow('output',img)
cv2.waitKey(0)
cv2.imwrite('Solar_systemwithname.jpg',img)