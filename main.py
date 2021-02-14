class Birthday_candles():
    def __init__(self, arr):
        self.arr = arr


    def counting_tallest(self):
        tallest = 0
        height = max(self.arr)
        for i in range(0, len(self.arr)):
            if self.arr[i] == height:
                tallest += 1
        return tallest
