#need self do it again!!
def flatten(dictionary):
	stack = [((), dictionary)]
	result = {}
	while stack:
		path, current = stack.pop()
		for k, v in current.items():
			if isinstance(v, dict) and v!={}:
				print("stack1=",stack)
				print("path=",path)
				print("k=",k)
				print("v=",v)
				stack.append((path + (k,), v))
				print("stack2=",stack)
			else:
				if v=={}:
					v=""
				result["/".join((path + (k,)))] = v
	print("result=",result)
	return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
          	
          	
          	
          	