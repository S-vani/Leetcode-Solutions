class Solution:
    def convert(self, s: str, numRows: int) -> str:
        times = 1
        n = 0
        zigzag = []
        while n < len(s):
            lst = [""]*numRows
            original_n = n
            i = 0
            while n < numRows + original_n and n < len(s):
                lst[i] = s[n]
                i += 1
                n += 1
            zigzag.append(lst)
            z = numRows-2
            while z > 0 and n < len(s):
                lst1 = [""]*numRows
                lst1[z] = s[n]
                zigzag.append(lst1)
                n += 1
                z -= 1
        final_str = ""
        curr_row = 0
        while curr_row < numRows:
            for i in range(len(zigzag)):
                final_str += zigzag[i][curr_row]
            curr_row += 1

        return final_str


            