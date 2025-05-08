# Extra lecture to clarify https://cs50.harvard.edu/python/2022/weeks/7/
import re


# Basic patterns
assert re.match(r"A", "A")
assert re.match(r"AB", "AB")
assert not re.match(r"AB", "A")
assert re.match(r"AB1", "AB1")
assert re.match(r"AAAAAAAAAAAAAA", "AAAAAAAAAAAAAA")
# Impractical, let's use proper regex:
assert re.match(r"A*", "AAAAAAAAAAAAAA")
assert re.match(r"A*", "")
assert re.match(r"A+", "A")
assert re.match(r"A+B+", "AB")
assert re.match(r"A+B+", "AAABBBBBB")

# Basic operators: *
assert re.match(r"A*", "")
assert re.match(r"A*", "AAAAAAAAAAA")

# Basic operators: +
assert not re.match(r"A+", "")
assert re.match(r"A+", "A")
assert re.match(r"A+", "AAAAAAAAAAA")

# Basic operators: ?
assert re.match(r"A?", "")
assert re.match(r"A?", "A")
assert re.match(r"AB?", "A")
assert re.match(r"AB?", "AB")
assert re.match(r"A+B?", "AAAA")
assert re.match(r"A+B?", "AAAAB")

# Basic operators: .
assert re.match(r".", "A")
assert re.match(r".", "!")
assert re.match(r"A.B", "AxB")
assert re.match(r"A.B", "A!B")
assert re.match(r".*", "")
assert re.match(r".*", "abcdef!#$")

# Basic operators: ()
assert re.match(r"(AB)?C", "C")
assert re.match(r"(AB)?C", "ABC")
assert re.match(r"(12)*3", "3")
assert re.match(r"(12)*3", "123")
assert re.match(r"(12)*3", "1212123")

# Basic operators: | and ()
assert re.match(r"A|B", "A")
assert re.match(r"A|B", "B")
assert re.match(r"A1|2B", "A1")
assert re.match(r"A(1|2)B", "A2B")
assert re.match(r"(AB|CD)", "CD")
assert re.match(r"(A|B)|(C|D)", "AC")
assert re.match(r"(A|B)|(C|D)", "AD")
assert re.match(r"(A|B)|(C|D)", "BC")
assert re.match(r"(A|B)|(C|D)", "BD")
assert re.match(r"(1|2)*3", "23")
assert re.match(r"(1|2)*3", "211112211111113")

# Basic operators: []
assert re.match(r"[ABCDE]", "C")
assert re.match(r"[!$]", "$")
assert re.match(r"[ABCDE]+", "ABEDE")
assert re.match(r"[A-Z]+", "ABKDFJKDJF")
assert re.match(r"[A-Za-z]+", "akdjfkKJDKJFdjfakdf")
assert re.match(r"[^AB]+", "CD")

# Basic operators: [] shorthands
assert re.match(r"[0-9]+", "38483489384")
assert re.match(r"\d+", "38483489384")

assert re.match(r"[^0-9]+", "abc")
assert re.match(r"\D+", "abc")

assert re.match(r"[A-Za-z0-9_]+", "abcABC123")
assert re.match(r"\w+", "abcABC123")

assert re.match(r"hello there", "hello there")
assert re.match(r"hello +there", "hello       there")
assert re.match(r"hello\s+there", "hello       there")


# Basic operators: ^, $
assert not re.match(r"^(A|B)$", "AB")
assert re.match(r"^(A|B)(A|B)$", "AB")


# Basic operators: {n}, {n, m}
assert re.match(r"^(A|B){2}$", "AB")
assert re.match(r"^(A|B){2,4}$", "ABBA")






# ******** Switch to show on computer from this point ********

# Options: ignore case
assert re.match(r"(hello|HELLO) my friend", "HELLO my friend")
assert re.match(r"hello my friend", "hello my friend", re.IGNORECASE)

assert re.match(r"(hello|h*|\w+), welcome to our bank!", "hi, welcome to our bank!")
assert re.match(r"""
                (hello|h*|\w+)          # This is the greeting, it can be hello, anything starting with h or other
                ,\swelcome\sto\sour\sbank
                (\.|!)?                 # Sentence can optionally end with period or exclamation point.
                """,
                "hi, welcome to our bank!", re.VERBOSE)



# Showcase on whiteboard + regex101.com on essentials to understand how to
# approach problem https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
#
# See regex101 tests (log in with my Github account before clicking private URL):
# * https://regex101.com/r/ScuZVQ/5 
# * https://regex101.com/r/PaeWpJ/1