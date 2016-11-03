import imutils


def pyramid(image, scale=1.5, minSize=(30,30)):
    """
    Create a succesive list of increasing smaller images aka a pyramid

    :param image: Valid image
    :param scale: Decrease scale factor (float). Larger scale = more decreasing (reaches minSize quicker)
    :param minSize: Minimum image size
    """
    yield image                                                        #initial image is original

    while True:
        yield image
        w = int(image.shape[1] / scale)                                #recursively scale the width down 2/3 (divided 150%)
        image = imutils.resize(image, width=w)                         #return a aspect-ratio maintained scaled image

        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]: #check for minimum scale, if yes don't return new image
            break

        yield image                                                    #create list of recursively scaled images aka the pyramid


def sliding_window(image, stepSize, windowSize):
    """
    Generate slices of image using windows that slide and resize

    :param image: Source Image
    :param stepSize: How many pixels to skip per slide
    :param windowSize: Size of image window
    """

    for row in xrange(0, image.shape[0], stepSize):
        for col in xrange(0, image.shape[1], stepSize):
            yield (col, row, image[row:row + windowSize[1],col:col + windowSize[0]])