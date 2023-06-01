def facorial(number : int)->int:
    """
    This function will return factorial of provided 'number'
    :param number: User input will be integer
    :return: integer
    """
    result = 1
    if number == 0:
        return result
    else:

        for value in range(1,number+1):
            result*= value
        return  result


for value in range(1,37):
    print("{0} {1}".format(value,facorial(value)))
