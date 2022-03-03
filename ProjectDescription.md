## A web front that mimics an online store with a back-end Database system. 
An online business maintains a large collection of antiques and collectables stored in various repositories around the world. The business sells these items through its online store and also through a variety of online auction houses. The business is facing an operational problem that sometimes an item might be sold more than once to different customers as the information is relayed to all the other online facilities by email and administrators of the various auction houses have to search for the sold item and remove it from their lists manually. The ensuing delays might lead to a duplicate sale and thus might compromise the integrity and the reputation of the company as it’ll be exposed to negative criticism and possible law suits. Furthermore the company’s partner action houses have started complaining and have threatened to withdraw from the partnerships if such issues and complaints continue as such situations undermine their reputation too.

To resolve such conflicts the company has tasked you to design and develop appropriate software that utilises suitable data structures and relevant algorithms that would process the data to complete the following tasks.


* New items can be added to a repository and removed from it at any point in time
    *	The company would like to keep the placing of items in a repository as transparent as possible to the users, but expects that maximum efficiency in searching and finding an item can be achieved when there is a need to remove it.
    *	The same item can be present in many repositories and can form part of many sets of items – e.g. a coin can be part of a set of coins or can be offered elsewhere as an individual coin; likewise a piece of furniture or a piece of clothing.
*	Items will need to be deleted from all repositories once they are sold regardless of where they are sold at. If an item is part of a set it should be removed from the set.
*	All items are individually identified – even if they are of the same type, e.g. where multiples copies of the same coin exist.
*	If an item is removed from a set an item of the same type should sought through the various repositories to complement the set. You can assume that the physical location of the item is irrelevant in this case.

