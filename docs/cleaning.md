# Cleaning 
_first step_

Before feeding the data into the algorithm, the chat data is cleaned by a
function `cleanText` which removes all the emoji's and non-utf8 characters from the data.

`myfunctions.chatParser.cleanText()`

# cleanText(filename)

**filename**: Takes one argument that is the name of the chat file.

**return** : a List containing the strings of the whatsapp conversation.


