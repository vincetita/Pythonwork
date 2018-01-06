class student:
    def details(self, name,age):
        self.name=name
        self.age=age
        print("The name is {} and the age is {}".format(name,age))

st=student()
st.details("Asamba",20)
print(st.name, st.age)