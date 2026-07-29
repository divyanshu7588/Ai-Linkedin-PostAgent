
from graph import graph
from agents.email import send_email

result = graph.invoke({})

send_email(
    result["post"],
    result["image"]
)
# post = result["post"]
#
# send_email(post)
# from graph import graph
#
# result = graph.invoke({})
#
# print(result)
# print(type(result))
# print(type(result["post"]))
# print(result["post"])