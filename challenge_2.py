"""
With your birthday coming up soon, your eccentric friend sent you a message to say "happy birthday":

>>> message :
    hhhappyyyy biirrrrrthddaaaayyyyyyy to youuuu
    hhapppyyyy biirtttthdaaay too youuu
    happy birrrthdayy to youuu
    happpyyyy birrtthdaaay tooooo youu

At first, it looks like a song, but upon closer investigation, you realize that your friend hid the phrase "happy birthday" thousands of times inside his message. In fact, it contains it more than 2 million times! To thank him, you'd like to reply with exactly how many times it occurs.

To count all the occurences, the procedure is as follows: look through the paragraph and find a 'h'; then find an 'a' later in the paragraph; then find an 'p' after that, and so on. Now count the number of ways in which you can choose letters in this way to make the full phrase.

More precisely, given a text string, you are to determine how many times the search string appears as a sub-sequence of that string.

Write a function called countSubsequences that takes two arguments: needle, the string to be search for and haystack, the string to search in. In our example, "happy birthday" is the needle and the birthday message is the haystack. The function should return the number of times needle occurs as a sub-sequence of haystack. Spaces are also considered part of the needle.

Since the answers can be very large, return only the last 8 digits of the answer in case it exceeds 8 digits. The answers to the test cases will all be shorter than 8 digits.

"""


def countSubsequences(needle, haystack):
    # Initialize a 2D array to store the count of subsequences
    dp = [[0] * (len(haystack) + 1) for _ in range(len(needle) + 1)]

    # Base case: empty needle matches all characters in haystack once
    for j in range(len(haystack) + 1):
        dp[0][j] = 1

    # Dynamic programming to fill the dp array
    for i in range(1, len(needle) + 1):
        for j in range(1, len(haystack) + 1):
            # If characters match, either include or exclude current character of haystack
            if needle[i - 1] == haystack[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                # If characters don't match, skip current character of haystack
                dp[i][j] = dp[i][j - 1]

    # Return the count of subsequences (last 8 digits if greater than 8 digits)
    return dp[-1][-1] % 100000000


def run_tests() -> None:
    """
    Runs the tests for the ``first_non_repeating_letter`` function.
    :return:
    """

    # Test the function
    needle = "happy birthday"
    haystack = ("hhhappyyyy biirrrrrthddaaaayyyyyyy to youuuu hhapppyyyy biirtttthdaaay too youuu happy birrrthdayy to "
                "youuu happpyyy birrtthdaaay tooooo youu")
    # print(countSubsequences(needle, haystack))
    print(f"{needle} occurs {countSubsequences(needle, haystack)} times in {haystack}")


if __name__ == '__main__':
    run_tests()
