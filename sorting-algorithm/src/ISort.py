from abc import ABCMeta, abstractmethod

# 排序接口
class ISort(metaclass=ABCMeta):
    # 默认排序方法
    @abstractmethod
    def sort(self, nums):
        pass
