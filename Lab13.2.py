class ENTERPRISE:
    def __init__(self, name, finance, year, owner):
        self.name = name
        self.finance = finance
        self.year = year
        self.owner = owner

    def SetFinance(self, new_finance):
        self.finance = new_finance

    def GetFinance(self):
        return self.finance

    def DisplayAll(self):
        return f"Name: {self.name}, Finance: {self.finance} thousand grn, Year: {self.year}, Owner: {self.owner}"

    def SetOwner(self, new_owner):
        self.owner = new_owner

    def GetOwner(self):
        return self.owner

def main():
    enterprises = [
        ENTERPRISE("Enterprise1", 1200, 1990, "Owner1"),
        ENTERPRISE("ПEnterprise2", 800, 2000, "Owner2"),
        ENTERPRISE("Enterprise3", 1500, 2010, "Owner1"),
        ENTERPRISE("Enterprise4", 200, 2015, "Owner3"),
        ENTERPRISE("Enterprise5", 3000, 1995, "Owner2"),
    ]

    print("Підприємства з активами більше 1 млн грн:")
    for enterprise in enterprises:
        if enterprise.GetFinance() > 1000:
            print(enterprise.DisplayAll())

    owner_count = {}
    for enterprise in enterprises:
        owner = enterprise.GetOwner()
        if owner in owner_count:
            owner_count[owner] += 1
        else:
            owner_count[owner] = 1

    print(" Власники, що мають більше одного підприємства:")
    for owner, count in owner_count.items():
        if count > 1:
            print(owner)

if __name__ == "__main__":
    main()
