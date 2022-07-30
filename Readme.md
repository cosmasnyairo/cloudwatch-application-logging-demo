# Simple Store 

Demo store to showcase logging to a file and to cloudwatch

## Table of contents

- [Product Module](#product-module)
- [Discount Module](#discount-module)
- [Cart Module](#cart-module)
- [Requirements](#requirements)

### Product Module:
We do the following actions on the product class: add, remove, fetch all produts and add a single product.

```json
// Sample product:
 {
        "productid": 1,
        "name": "mouse",
        "description": "Wireless and has rgb",
        "price": 4000,
        "stockquantity": 30
},
```

```mermaid
graph LR;
    UserInput-->id1(GetProducts);
    UserInput-->id2(GetSingleProduct);
    UserInput-->id3(AddProduct);
    UserInput-->id4(RemoveProduct);
    id1(GetProducts)-->id5(LogtoFile?);
    id2(GetSingleProduct)-->id5(LogtoFile?);
    id3(RemoveProduct)-->id5(LogtoFile?);
    id4(RemoveProduct)-->id5(LogtoFile?);
    id5(Log to file?)-->|YES|id6(Log to file);
    id5(Log to file?)-->|NO|id7(Log to cloudwatch);
``` 
### Discount Module:
We do the following actions on the discount class: add, remove, fetch all discounts

```json
// Sample discount:
{
    "name": "20% Off select items",
    "productid": 1,
    "discountpercentage": 20,
    "discountcode": "20FOR20"
},
```

```mermaid
graph LR;
    UserInput-->id1(GetDiscount);
    UserInput-->id2(AddDiscount);
    UserInput-->id3(RemoveDiscount);
    id1(GetDiscount)-->id5(LogtoFile?);
    id2(AddDiscount)-->id5(LogtoFile?);
    id3(RemoveDiscount)-->id5(LogtoFile?);
    id5(Log to file?)-->|YES|id6(Log to file);
    id5(Log to file?)-->|NO|id7(Log to cloudwatch);
``` 

### Cart Module:
We do the following actions on the cart class: add, remove, fetch all cart items

```json
// Sample cart:
{
    "productid": 4,
    "quantity": 10,
    "totalprice": 2000,
    "discountcodes": "50OFFERNOW",
    "date": "August 11, 2022"
},
```
    
```mermaid
graph LR;
    UserInput-->id1(GetCart);
    UserInput-->id2(AddtoCart);
    UserInput-->id3(RemovefromCart);
    id1(GetCart)-->id5(LogtoFile?);
    id2(AddtoCart)-->id5(LogtoFile?);
    id3(RemovefromCart)-->id5(LogtoFile?);
    id5(Log to file?)-->|YES|id6(Log to file);
    id5(Log to file?)-->|NO|id7(Log to cloudwatch);
``` 

### Requirements
- [Requirements.txt](requirements.txt) file contains all the packages that were used in creating of the blockchain and the api
