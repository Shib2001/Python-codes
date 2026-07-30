#dictionries are used to store data values in key:value pairs 
#They are unordered , mutable , and don't alllow duplicate keys 


# mint = {
#     "name" : "shrahdgshgas",
#     "cgpa":9.7878,
#     "marks":[98,7878,8939],
#     "annual scores":(877,8943843,4378347)
# }




# mint["name"] = "shiv kumar jha"

# print(mint)



#__________________________________________________________________________________________________________________

#Nested distcionary ( Basically objects hi hai yeh )

Sint = {
    "name" : "shrahdgshgas",
    "score":{
        "maths":{
            "1st-year":89,
            "2nd-year":90,
            "3rd-year":80
        },
        "english":{
            "1st-year":899,
            "2nd-year":980,
            "3rd-year":880
        }
    },
    "sports":{
        "played":["football","basketball"]
    }
}


print(Sint)