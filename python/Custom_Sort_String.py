class Solution:
    def customSortString(self, order: str, str: str) -> str:
        # merge sort
        return self.sort(order, str)
    def compare(self, order, a, b):
        if a not in order and b in order:
            return False
        elif a in order and b not in order:
            return True
        elif a not in order and b not in order:
            return True
        else:
            if order.index(a) <= order.index(b):
                return True
            else:
                return False
    def sort(self, order, str):
        if len(str) > 2:
            split = int(len(str)/2)
            return self.merge(order, self.sort(order, str[:split]), self.sort(order, str[split:]))
        else:
            if len(str) == 1:
                return str
            else:
                if self.compare(order, str[0], str[1]):
                    return str
                else:
                    return str[1] + str[0]
    def merge(self, order, firstStr, SecondStr):
        f_idx = 0
        s_idx = 0
        new_str = ""
        while f_idx < len(firstStr) and s_idx < len(SecondStr):
            if self.compare(order, firstStr[f_idx], SecondStr[s_idx]):
                new_str += firstStr[f_idx]
                f_idx += 1;
            else:
                new_str += SecondStr[s_idx]
                s_idx += 1
        if f_idx == len(firstStr):
            new_str += SecondStr[s_idx:]
        else:
            new_str += firstStr[f_idx:]
        # print(" new: {}".format(new_str))
        return new_str
    
