class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}

        # First and last occurrence of every character
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        # Find the smallest valid interval starting at each character
        for ch in first:
            start = first[ch]
            end = last[ch]

            i = start
            valid = True

            while i <= end:
                curr = s[i]

                # This character appeared before our start
                if first[curr] < start:
                    valid = False
                    break

                # Expand interval if necessary
                end = max(end, last[curr])
                i += 1

            if valid:
                intervals.append((start, end))

        # Earliest finishing interval first
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end

        return result