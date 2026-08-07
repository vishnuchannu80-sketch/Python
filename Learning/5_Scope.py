global_variable = "I am a global variable" # Global

def outer_function():
    # Enclosing
    enclosing_var = "I am an enclosing variable"
    
    def inner_function():
        # Local
        local_var = "I am a local variable"
        print(global_variable)  # Accessing global variable
        print(enclosing_var)  # Accessing enclosing variable
        print(local_var)  # Accessing local variable
        print(len([1,2,3,4]))
    
    inner_function()
outer_function()