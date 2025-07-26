class FamilyMember:
    def __init__(self, name, age, relation):
        self.name = name
        self.age = age
        self.relation = relation

    def show_info(self):
        print(f"\n Family Member Details")
        print(f"Name     : {self.name}")
        print(f"Age      : {self.age}")
        print(f"Relation : {self.relation}")

# Create objects for each family member
member1 = FamilyMember("Kusuma", 22, "Daughter")
member2 = FamilyMember("Gowramma", 40, "Mother")
member3 = FamilyMember("Akash", 19, "Brother")

# Display information
member1.show_info()
member2.show_info()
member3.show_info()
