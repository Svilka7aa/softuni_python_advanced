def start_spring(**kwargs):
    result = ""
    spring_objects = {}
    for key, value in kwargs.items():
        if value not in spring_objects:
            spring_objects[value] = []
        spring_objects[value].append(key)

    sorted_collection = sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0]))

    for i in sorted_collection:
        type_object = i[0]
        list_object = i[1]
        sorted_list_object = sorted(list_object)
        result += f"{type_object}:\n"
        for obj in sorted_list_object:
            result += f"-{obj}\n"
    return result


print("-" * 50)
example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

print("-" * 50)
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

print("-" * 50)
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
