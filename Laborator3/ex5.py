def validate_dict(rules,dictionary):
    for key,prefix,middle,suffix in rules:
        if key not in dictionary:
            return False
        val=dictionary[key]
        if not val.startswith(prefix):
            return False 
        if not val.endswith(suffix):
            return False 
        if middle not in val[1:-1]:
            return False 
    return True 

rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionary = {
    "key1": "come inside, it's too cold out",
    "key2": "start of winter is here",
    "key3": "this is not valid"
}
rez=validate_dict(rules,dictionary)
print(rez)