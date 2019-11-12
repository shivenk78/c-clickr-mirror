class Phone:

    uin = 0
    top_centroid_x = 0.0
    top_centroid_y = 0.0
    bottom_centroid_x = 0.0
    bottom_centroid_y = 0.0
    pixel_array = []


    def __init__(self, set_uin, set_top_centroid_x, set_top_centroid_y, set_bottom_centroid_x, set_bottom_centroid_y, set_pixel_array):
        self.uin = set_uin
        self.top_centroid_x = set_top_centroid_x
        self.top_centroid_y = set_top_centroid_y
        self.bottom_centroid_x = set_bottom_centroid_x
        self.bottom_centroid_y = set_bottom_centroid_y
        pixel_array = set_pixel_array