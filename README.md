# Budget Classifier API

## Overview

This API uses a NLP text classifier to predict a budget tracker entry's category based on it's description.

The API accepts JSON requests where the request body looks like this:

```
{
	"data": [
		{
			"description":"bagel and coffee breakfast"
		},
		{
			"description":"plane ticket to london"
		}
	]
}
```

The API parses the descriptions and returns a response like: 

```
[
    {
        "description": "bagel and coffee breakfast",
        "predicted_category": "Dining Out"
    },
    {
        "description": "plane ticket to london",
        "predicted_category": "Travel"
    }
]
```

The current categories for prediction are based on training from Jesse's budget tracker entries; there is currently no support to define your own categories.  Planning to add this in the future.

This API works closely with a "front-end" app [here](https://github.com/jginsberg3/budget-classifier-webapp) but can be used seperately also.
