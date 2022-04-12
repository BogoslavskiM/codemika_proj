class Question:

    def __init__(self, id: int, text: str, answer: str = None):
        self.__id = id
        self.__text = text
        self.__answer = answer

    def __str__(self):
        return self.__text

    def get_info(self):
        return {'id': self.__id, 'text': self.__text, 'answer': self.__answer}

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_value):
        pass

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_value):
        if isinstance(new_value, str):
            self.__text = new_value

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, new_value):
        if isinstance(new_value, str):
            self.__answer = new_value

    def get_content(self):
        return self.__str__()


class Container:  # этим классом можно описать и игру, и уровень и тему и др, т.к. у нас для каждого объекта в С свой id

    def __init__(self, id: int, name: str, description: str = None):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__content = list()

    def __str__(self):
        return self.__name

    def get_info(self):
        return {'id': self.__id, 'name': self.__name, 'description': self.__description}

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_value):
        pass

    @property
    def name(self):
        return f'{self.__id}: {self.__name}'

    @name.setter
    def name(self, new_value):
        if isinstance(new_value, str) and len(new_value) <= 100:
            self.__name = new_value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_value):
        if isinstance(new_value, str) or new_value is None:
            self.__description = new_value

    def get_title(self):
        return self.__content

    def add_content(self, id: int):
        self.__content.append(id)

    def pop_content(self, id: int):
        self.__content.remove(id)


class User:

    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        self.__favorites = []


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_value):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        if isinstance(new_value, str) and len(new_value) <= 100:
            self.__name = new_value

    @property
    def favorites(self):
        return self.__favorites

    @favorites.setter
    def favorites(self, new_value):
        pass

    def add_favorite(self, valid_obj_id):
        self.__favorites.append(int(valid_obj_id))

    def pop_favorite(self, id):
        if id in self.__favorites:
            self.__favorites.remove(id)


class App:

    def __init__(self):
        self.__users = dict()
        self.__last_u = 0
        self.__objects = dict()
        self.__last_o = 0
        self.__content = list()

    def add_user(self, name: str):
        id = self.__last_u + 1
        self.__last_u += 1
        user = User(name, id)
        self.__users[id] = user
        return id

    def add_question(self, place: int, text: str, answer: str = None):
        id = self.__last_o + 1
        self.__last_o += 1
        question = Question(id, text, answer)
        self.__objects[id] = question
        if place == 0:
            self.__content.append(id)
        elif place in self.__objects.keys():
            self.__objects[place].add_content(id)
        return id

    def add_container(self, place: int, name: str, description: str = None):
        id = self.__last_o + 1
        self.__last_o += 1
        container = Container(id, name, description)
        self.__objects[id] = container
        if place == 0:
            self.__content.append(id)
        elif place in self.__objects.keys():
            self.__objects[place].add_content(id)
        return id

    def add_favorite(self, user_id: int, obj_id: int):
        self.__users[user_id].add_favorite(obj_id)

    def pop_favorite(self, user_id: int, obj_id: int):
        self.__users[user_id].pop_favorite(obj_id)

    def get_title(self):
        return self.__content

    def get_content(self, id):
        return self.__objects[id].get_title()

    def __str__(self):
        c = ''
        for i in self.__objects.values():
            c += str(i) + '\n'
        return c


app = App()
my_id = app.add_user('makar')
test_container_id = app.add_container(0, 'test_contrainer')
id = app.add_container(test_container_id, 'test_container_2', 'hello')
q_id = app.add_question(id, 'как живешь?')
app.add_favorite(my_id, q_id)
print(app)

