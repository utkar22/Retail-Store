import axios from "axios";
import { useEffect, useState } from "react";

import Product from "../../components/Product";
import cart from "../../util/cartData";

import './CartProducts.css'

export default () => {
	const [productList, setProductList] = useState()
	const [loaded, setLoaded] = useState("not")
	const [total, setTotal] = useState(0);

	useEffect( () => {
		(async () => {
			let tempProductList = []
			try {
				let tempTotal = 0

				let productArray = (await axios.get(`/api/cart/`, {
					headers: {
						authorization: sessionStorage.getItem('user-token')
					}
				})).data.cart
				cart.length = 0
				console.log(productArray)
				for (let i = 0; i < productArray.length; i++) {
					console.log("total",total)
					tempTotal += Number(productArray[i].price)
					tempProductList.push(<Product key={productArray[i].product_id} id={productArray[i].product_id}  productName={productArray[i].name}
												  productPrice={productArray[i].price} />)
					
					cart.push(productArray[i].product_id)
					console.log(productArray[0].name, productArray[0].price)
				}
					setProductList(tempProductList)
				setTotal(tempTotal)
				setLoaded("done")
			}
			catch (err){
				if (err)
					console.error(err)
			}
			console.log("fusses",total)
		})()
		console.log("cart products")
	},
	[total, loaded])

	return (
		<>
			<span className="cart-total">{"Price : $"+total}</span>
			<div id="cart-products">
				{ productList}
				{/*<TransactionItems transaction = {total}/>*/}
			</div>
		</>
	)
}