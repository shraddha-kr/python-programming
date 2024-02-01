# https://py.checkio.org/en/mission/the-cheapest-flight/
def cheapest_flight(costs: list, a: str, b: str) -> int:
    cheap_fare = -1
    # cheap flight found
    for el in costs:
        if((costs[0]==a and costs[1]==b) or (costs[0]==b and costs[1]==a)):
            # every subsequent iteration after first
            if((cheap_fare > 0) and (cheap_fare > costs[2])):
                cheap_fare = costs[2]
                return cheap_fare
            elif((cheap_fare > 0) and (cheap_fare < costs[2])):
                return che
            # no flight found, return 0
        else:
            return 0


print("Example:")
# print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C"))

# # These "asserts" are used for self-checking
# assert (
#     cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
# )
# assert (
#     cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
# )
# assert (
#     cheapest_flight(
#         [
#             ["A", "C", 40],
#             ["A", "B", 20],
#             ["A", "D", 20],
#             ["B", "C", 50],
#             ["D", "C", 70],
#         ],
#         "D",
#         "C",
#     )
#     == 60
# )
# assert (
#     cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
# )
# assert (
#     cheapest_flight(
#         [["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D"
#     )
#     == 25
# )

# print("The mission is done! Click 'Check Solution' to earn rewards!")
