<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Amazon Old Style - Ultra Retro 2000s</title>
<style>
body { font-family:"Trebuchet MS", Arial, sans-serif; margin:0; background-color:#f0f0f0; color:#000; }
header { background-color:#131921; color:white; padding:10px; display:flex; align-items:center; justify-content:space-between; position:relative; flex-wrap:wrap; }
header img { height:40px; transition: transform 0.3s; }
header img:hover { transform: scale(1.1); }
.search-bar { flex:1; display:flex; margin:0 20px; min-width:200px; }
.search-bar input { width:100%; padding:8px; border:1px solid #ff9900; }
.search-bar button { padding:8px 12px; background-color:#ff9900; border:1px solid #ff9900; cursor:pointer; transition: background 0.3s; }
.search-bar button:hover { background-color:#f7b500; }
#deal-banner { background:#ff9900; color:#000; padding:5px 10px; font-weight:bold; overflow:hidden; white-space:nowrap; box-sizing:border-box; animation:scroll 10s linear infinite; }
@keyframes scroll { 0% { transform:translateX(100%); } 100% { transform:translateX(-100%); } }
nav { background-color:#232f3e; color:white; padding:8px; font-size:14px; display:flex; }
nav a { color:white; text-decoration:none; margin-right:15px; display:flex; align-items:center; transition: transform 0.2s; }
nav a img { width:18px; height:18px; margin-right:5px; }
nav a:hover { text-decoration:underline; transform: translateY(-2px); }
.container { padding:20px; }
h2 { border-bottom:2px solid #ccc; padding-bottom:5px; margin-bottom:15px; }
.products { display:grid; grid-template-columns:repeat(auto-fill,minmax(180px,1fr)); gap:15px; }
.product { border:1px solid #ccc; background:white; padding:10px; text-align:center; box-shadow:1px 1px 3px #ccc; transition: transform 0.3s, box-shadow 0.3s; position:relative; }
.product:hover { transform: scale(1.05); box-shadow:2px 2px 8px #aaa; }
.product img { max-width:100%; height:150px; object-fit:contain; margin-bottom:8px; transition: transform 0.3s; }
.product img:hover { transform: scale(1.1); }
.badge { position:absolute; top:5px; right:5px; background:red; color:white; padding:2px 5px; font-size:12px; font-weight:bold; animation:blink 1s infinite; }
@keyframes blink { 0%,50%,100%{opacity:1;} 25%,75%{opacity:0;} }
.product button { background-color:#ff9900; border:1px solid #a88734; padding:6px 10px; cursor:pointer; font-size:14px; transition: background 0.3s, transform 0.2s; }
.product button:hover { background-color:#f7b500; transform: scale(1.05); }
.cart-section { margin-top:30px; border-top:2px solid #ccc; padding-top:15px; background:#fff; box-shadow:0 0 5px #aaa; transition: box-shadow 0.3s; }
.cart-section:hover { box-shadow:0 0 12px #888; }
table { width:100%; border-collapse:collapse; }
table th, table td { border:1px solid #ccc; padding:8px; text-align:center; }
.qty-btn { padding:3px 8px; margin:0 3px; cursor:pointer; border:1px solid #aaa; background:#eee; transition: background 0.2s; }
.qty-btn:hover { background:#ddd; }
table button.remove { background-color:#d9534f; color:white; border:none; padding:5px 10px; cursor:pointer; transition: background 0.3s; }
table button.remove:hover { background-color:#c9302c; }
button.clear-cart, button.checkout { margin:5px 5px 10px 0; padding:6px 12px; background:#d9534f; color:white; border:none; cursor:pointer; transition: background 0.3s, transform 0.2s; }
button.clear-cart:hover, button.checkout:hover { background:#c9302c; transform: scale(1.05); }
#cart-link { position:relative; cursor:pointer; font-weight:bold; transition: color 0.3s; }
#cart-link:hover { color:#ff9900; }
#mini-cart { display:none; position:absolute; top:25px; right:0; background:white; border:1px solid #ccc; width:260px; padding:10px; z-index:100; box-shadow:2px 2px 6px #888; transition: background 0.3s; }
#mini-cart:hover { background:#f9f9f9; }
#mini-cart ul { list-style:none; padding:0; margin:0; max-height:200px; overflow-y:auto; }
#mini-cart li { border-bottom:1px solid #eee; padding:3px 0; display:flex; justify-content:space-between; transition: background 0.3s; }
#mini-cart li:hover { background:#f0f0f0; }
#mini-cart li span { font-weight:bold; }
footer { margin-top:30px; background:#131921; color:white; text-align:center; padding:15px; font-size:14px; }
</style>
</head>
<body>

<header>
<img src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg" alt="Amazon Logo">
<div class="search-bar">
<input type="text" placeholder="Search">
<button>Go</button>
</div>
<div id="cart-link">
<img src="https://upload.wikimedia.org/wikipedia/commons/5/55/Shopping_cart_font_awesome.svg" style="width:20px;height:20px;margin-right:5px">🛒 Cart (0)
<div id="mini-cart">
<ul id="mini-cart-list"></ul>
<p id="mini-cart-total"></p>
</div>
</div>
<div id="deal-banner">🔥 Deal of the Day! Limited Time Offer! 🔥</div>
</header>

<nav>
<a href="#"><img src="https://upload.wikimedia.org/wikipedia/commons/f/f7/Icon-gift.svg">Today's Deals</a>
<a href="#"><img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Icon-people.svg">Customer Service</a>
<a href="#"><img src="https://upload.wikimedia.org/wikipedia/commons/3/3e/Icon-box.svg">Registry</a>
<a href="#"><img src="https://upload.wikimedia.org/wikipedia/commons/6/62/Icon-giftcard.svg">Gift Cards</a>
</nav>

<div class="container">
<h2>Featured Products</h2>
<div class="products">
<div class="product" data-name="Learn HTML Book" data-price="9.99">
<div class="badge">Limited Stock!</div>
<img src="https://via.placeholder.com/150/ffeb3b/000000?text=Book" alt="Product">
<p>📖 Book: Learn HTML</p>
<p><b>$9.99</b></p>
<button>Add to Cart</button>
</div>
<div class="product" data-name="Classic Headphones" data-price="19.99">
<div class="badge">Limited Stock!</div>
<img src="https://via.placeholder.com/150/2196f3/ffffff?text=Headphones" alt="Product">
<p>🎧 Classic Headphones</p>
<p><b>$19.99</b></p>
<button>Add to Cart</button>
</div>
<div class="product" data-name="Old Style Mouse" data-price="7.49">
<div class="badge">Limited Stock!</div>
<img src="https://via.placeholder.com/150/4caf50/ffffff?text=Mouse" alt="Product">
<p>🖱️ Old Style Mouse</p>
<p><b>$7.49</b></p>
<button>Add to Cart</button>
</div>
<div class="product" data-name="Retro Keyboard" data-price="12.99">
<div class="badge">Limited Stock!</div>
<img src="https://via.placeholder.com/150/f44336/ffffff?text=Keyboard" alt="Product">
<p>⌨️ Retro Keyboard</p>
<p><b>$12.99</b></p>
<button>Add to Cart</button>
</div>
</div>

<div class="cart-section">
<h2>Your Cart</h2>
<button class="clear-cart" onclick="clearCart()">Clear Cart</button>
<button class="checkout" onclick="checkout()">Checkout</button>
<table id="cart-table">
<thead>
<tr>
<th>Product</th>
<th>Price</th>
<th>Qty</th>
<th>Total</th>
<th>Action</th>
</tr>
</thead>
<tbody></tbody>
</table>
<h3 id="cart-total">Grand Total: $0.00</h3>
</div>
</div>

<footer>
© 2000-2025 Old Amazon Clone — Ultra Retro 2000s
</footer>

<script>
let cart = JSON.parse(localStorage.getItem("cart")) || [];
function updateCart(){
let cartTable=document.querySelector("#cart-table tbody"); cartTable.innerHTML="";
let grandTotal=0;
cart.forEach((item,index)=>{
let total=(item.price*item.qty).toFixed(2); grandTotal+=parseFloat(total);
let row=document.createElement("tr");
row.innerHTML=`<td>${item.name}</td><td>$${item.price}</td><td><button class="qty-btn" onclick="changeQty(${index},-1)">-</button>${item.qty}<button class="qty-btn" onclick="changeQty(${index},1)">+</button></td><td>$${total}</td><td><button class="remove" onclick="removeItem(${index})">Remove</button></td>`;
cartTable.appendChild(row);
});
document.getElementById("cart-total").innerText="Grand Total: $"+grandTotal.toFixed(2);
document.getElementById("cart-link").childNodes[1].textContent="🛒 Cart ("+cart.reduce((a,b)=>a+b.qty,0)+")";
updateMiniCart();
localStorage.setItem("cart",JSON.stringify(cart));
}
function changeQty(index,change){ cart[index].qty+=change; if(cart[index].qty<=0) cart.splice(index,1); updateCart(); }
function removeItem(index){ cart.splice(index,1); updateCart(); }
function clearCart(){ if(confirm("Clear cart?")){ cart=[]; updateCart(); } }
function checkout(){ if(cart.length>0){ alert("✅ Order placed! Total: $"+cart.reduce((a,b)=>a+b.price*b.qty,0).toFixed(2)); cart=[]; updateCart(); }else alert("Cart is empty!"); }
document.querySelectorAll(".product button").forEach(btn=>{
btn.addEventListener("click",e=>{
let product=e.target.closest(".product");
let name=product.getAttribute("data-name");
let price=parseFloat(product.getAttribute("data-price"));
let existing=cart.find(item=>item.name===name);
if(existing) existing.qty++; else cart.push({name,price,qty:1});
updateCart();
});
});
const cartLink=document.getElementById("cart-link");
const miniCart=document.getElementById("mini-cart");
const miniCartList=document.getElementById("mini-cart-list");
const miniCartTotal=document.getElementById("mini-cart-total");
cartLink.addEventListener("mouseenter",()=>{ miniCart.style.display="block"; });
cartLink.addEventListener("mouseleave",()=>{ miniCart.style.display="none"; });
function updateMiniCart(){ miniCartList.innerHTML=""; let total=0; cart.forEach(item=>{ total+=item.price*item.qty; let li=document.createElement("li"); li.innerHTML=`<span>${item.name} x${item.qty}</span><span>$${(item.price*item.qty).toFixed(2)}</span>`; miniCartList.appendChild(li); }); miniCartTotal.textContent="Total: $"+total.toFixed(2); }
updateCart();
</script>

</body>
</html>
