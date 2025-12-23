import bisect
class ExamTracker:

    def __init__(self):
        self.times = []
        self.prefix_sums = [0]
    def record(self, time: int, score: int) -> None:
        
        self.times.append(time)
        self.prefix_sums.append(self.prefix_sums[-1] + score)
    def totalScore(self, startTime: int, endTime: int) -> int:
        # bisect là tìm kiếm nhị phận sử dụng tìm kiếm nhị phân để tìm dến giá trị start time theo sắp xếp
        # Khi cái lít nó luôn được append thì sẽ luôn tirleej với các score ở bên dưới thì bisect sẽ trả về đến giá trị đầu của eft vè giá trị của right - nói đơn giản bisisect left, right sẽ là tìm kiếm nhị phân của giá trị cần tìm đến bên phả và bên trái

        left_idx = bisect.bisect_left(self.times, startTime)
        right_idx = bisect.bisect_right(self.times, endTime)

        return self.prefix_sums[right_idx] - self.prefix_sums[left_idx]


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)