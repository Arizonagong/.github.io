# %%
def parent():
    print("printing parent()")
    def first_child():
        print("printing first_child()")
    first_child()
print(parent())

# %%
