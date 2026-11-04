class Solution:

    def encode(self, strs: List[str]) -> str:

        encode_string = [f"{len(s)}#{s}" for s in strs]

        return "".join(encode_string)


    def decode(self, s: str) -> List[str]:

        result = []

        i = 0

        while i <= len(s) - 1:

            j = i
            while s[j].isdigit():
                j += 1

            len_convention = 2
            if len(s[i:j]) > 1:
                len_convention += len(s[i:j]) - 1

            next_char = int(s[i:j])
            next_index = i + next_char + len_convention
            start_index = i + len_convention

            result.append(s[start_index:next_index])

            i = next_index

        return result


# strs = ["Hello","World"]
strs=["we","say",":","yes","!@#$%^&*()"]

encode_string = Solution().encode(strs)
decode_strs = Solution().decode(encode_string)

print("encode_string: ", encode_string)
print("decode_strs: ", decode_strs)