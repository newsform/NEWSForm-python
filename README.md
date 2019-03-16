# NEWSForm-python
This python module offers an interactive way to create and manipulate data stored with NEWSForm standard in JSON. 

# Methods
## Initialization
Creates a new NEWSForm object.
Argument list:

(Optional) string: the NEWSForm JSON string. If not specified, the new object would be empty.
(Optional, default: false) isDecentralized: the NEWSForm could be decentralized. If this argument is true, the file will be optimized using decentralized algorithms. You can select these algorithms using latermentioned parameters.
(Optional) decentralizationAlgo: This argument is necessary if `isDecentralized` is set to `true`. The following algorithms are available: HAM[TODO]
(Optional) metaData: specify metadata component of this NEWSForm object. The type of this argument is `NFMeta`. You must provide the data if you want the NEWSForm object to be complete.

## Manipulation: update
Update the NEWSForm file with the updated data. 
Argument list:
(Optional) timestamp: Update metadata with the timestamp provided. Necessary if using decentralized algorithm.
(Required) data:  

# Roadmap
- NEWSForm server: run as command-line and provides a RESTFul API for front-end ppl to use. OOF JAVASCRIPT TIME
- Decentralized support: implement HAM algorithm support for decentralized programs (such as GUN.js) to use. (And write the docs (which I never do))
