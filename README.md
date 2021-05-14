# Session 2 assignment of EPAi3.0
# Cyclic Referencing and String Interning

## Cyclic references

Sometimes we need to build relationships that are two way in nature, and this can be done by using parent child objects linked through referencing with the help of pointers. However, this can very easily lead to memory mismanagement and leaks if not done right. This repository serves as an example to showcase things that need to be taken into account while working with referenced objects.

### Classes

1. __Something__ - The base object that contains reference to SomethingNew instance

    > Attributes
    > something_new - reference pointer to the assosciated SomethingNew instance

    > Methods
    > __init__ : initializes the something_new reference to None
    > __repr__ : Provides the name of object along with its memory address

2. __SomethingNew__ - The child object that contains its index in the collection of Something

    > Attributes
    > i - index of object in collection
    > something - reference pointer to the Something instance it is tracking

    > Methods
    > __init__ : initializes the something_new reference to None
    > __repr__ : Provides the name of object along with its memory address

### Functions

1. __add_something__ - Appends a new instance of Something object (with its assosciated SomethingNew) to a collection of Something

    > Arguments
    > collection - the list of Something to append to
    > i - the index of the new Something instance
    
    > Returns
    > None

2. __clear_memory__ - clears the memory allocated to a list of Somethings

    > Arguments
    > collection - the list of Something to clear from memory
    
    > Returns
    > None

    __Note__ : This is a very important function which needs to invoke the Python Garbage Collector as well, to clear the object instances of Something and SomethingNew. These will otherwise be left behind as they are bound by cyclic references

3. __critical_function__ - Creates a long list of Something (1024 * 128 elements) and then clears it from memory. Serves as a function to monitor memory utilization. Internally calls add_something and clear_memory

    > Arguments
    > None
    
    > Returns
    > None

## String Interning

Python internally interns numbers from -5 to 256 and certain small strings as well. This means, these objects are always referenced to the same mempry location, and multiple instances do not create copies in memory. They just point to the same memory location to optimize memory usage. 

This becomes crucial when we want to do comparisons espescially with large strings, as it is significantly faster to check if two objects point to the same memory, as that would inevitably imply they are equal. This is done with the __is__ keyword instead of the == operator.

Another common way to speed up comparisons is hashing, which allows us to compare the hashes of the strings rather than the strings themselves.
The benefits of interning and hashing are benchmarked below.

### Functions

Four funtions have been built for the same purpose : Compare two large strings and then check if character 'd' is present in one of the strings for large number of iterations n.

> Arguments
> n - the number of times the comparison and check needs to be made
    
> Returns
> None

1. __compare_strings_old__ - This function is really slow, more than running a 6 seconds sleep. (time.sleep(6)).
Highly inefficient due to the following :
    - Does not intern and hence uses == operator
    - Compares strings using a character list breakdown char_list instead of checking directly in the string itself.
    - Runs two for loops instead of one

We fix second and third in the following variants of the function, but take varied options to optimize the first.

2. __compare_strings_new_hash__ - uses hashing of strings for comparison
3. __compare_strings_new_interned__ - interns the strings for comparison
4. __compare_strings_new_hash_interned__ - interns the hashes of the string for comparison

### Benchmarks

Using cProfiler we were able to get the cumulative run times for 3 iterations of 25 runs of the function with n = 10000000 and are tabulated below.

| ncalls | tottime | percall | cumtime | filename,lineno(function)|
| --- | ---- | --- | ---- | ---- |
| 75  | 80.762  |  1.077  | 80.762  | session2.py,116(compare_strings_new_hash) |
| 75 |  80.270  |  1.070  | 80.271  | session2.py:103(compare_strings_new_hash_interned) |
| 75  | __71.840__  |  __0.958__  |__71.841__  | session2.py,92(compare_strings_new_interned) |

The best function in terms of performace which is __compare_strings_new_interned__ has been assigned as __compare_strings_new__ for the assosciated test cases

### Test Case Results

The test cases have all passed as shown below.

![Test Cases](/test_cases_results.png)
