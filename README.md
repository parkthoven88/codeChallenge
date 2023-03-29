# Ventera Developer Challenge

Your team's client has just acquired a new company and has some questions about their recent sales. Your team was given a file, included in this repo as `data.json`, that contains some dummy data from the inventory system of the new company. Your team must develop a script or application that can answer the following:

1. Total revenue (sum of quantity times price of all items)
1. Vendor with the most revenue
1. Quantity of hats sold (items where the key is exactly 'hat')
1. ID of the customer that bought the most ice in October

Your team quickly realized the data structure is not particularly convenient to work with and also carries some personally identifiable information  (PII) unnecessarily. You white-boarded a transformation that the team liked:
```js
// Old format
{
    "id": 123,
    "vendor": "example",
    "customer": {
        "id": 321,
        "name": "John Doe",
        "address": "123 some st"
    },
    "order": {
        "foo": {
            "quantity": 1,
            "price": 1.5
        },
        "bar": {
            "quantity": 4,
            "price": 4
        }
    }
}
// New format\
{
    "id": 123,
    "vendor": "example",
    "customerId": 321,
    "details": [
        {
            "item": "foo",
            "quantity": 1,
            "price": 1.5,
            "revenue": 1.5
        },
        {
            "item": "bar",
            "quantity": 4,
            "price": 4,
            "revenue": 16
        }
    ]
}
```
To split the work, two stories were written, one to create a function that performs that transformation, and another to take care of answering the client's questions, which would accept the new data format for input.

You are expected to complete one or both of the stories. A version of `data.json` that has been already transformed is provided as `data-transformed.json` so either story can be executed on first.

## Tech details
- Solution can be written in Python (2.7 or 3+) or JavaScript (NodeJS 8+ preferred.) Document the version used.
- You may assume the data files are not too large to read into memory, that they contain valid JSON and is an array of objects containing at least the described fields with the same data types. Extensive error handling and validation is not necessary.
- There is no need to develop a user interface, it is acceptable to assume the input will be in the current directory as `data.json`, or `data-transformed.json` if only the second story is completed. If an interface is created provide clear instructions for its use.
- The output for either story can be a file or written to standard out, it must be valid JSON.
- Third party libraries are acceptable but should not be necessary, any setup required by the evaluator must be well documented. Bundling the libraries with your solution is acceptable as well.

## Evaluation Criteria
Your solution will be evaluated on the accuracy of the solution and the maintainability of the code first and foremost. Keep in mind you are working on a team and others will be extending this code in the future as requirements change.
