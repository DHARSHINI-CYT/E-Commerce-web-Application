import os

content = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LUXESTORE | Premium Goods</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Phosphor Icons -->
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <!-- React & ReactDOM (Development) -->
    <script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <!-- Babel for in-browser JSX compilation -->
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: #ffffff; color: #1e293b; }
        .hide-scrollbar::-webkit-scrollbar { display: none; }
        .hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
        /* Custom radio buttons */
        input[type="radio"] { accent-color: #000; }
    </style>
</head>
<body class="bg-white">
    <div id="root"></div>

    <script type="text/babel">
        const { useState, useEffect } = React;

        // --- COMPONENTS --- //

        const Sidebar = ({ activeTab, setActiveTab, cartCount }) => {
            const tabs = [
                { id: 'catalog', name: 'Shop Catalog', icon: 'storefront' },
                { id: 'cart', name: 'Shopping Cart', icon: 'shopping-cart', badge: cartCount },
                { id: 'checkout', name: 'Checkout', icon: 'credit-card' },
                { id: 'profile', name: 'My Profile', icon: 'user' },
                { id: 'admin', name: 'Inventory Admin', icon: 'kanban' }
            ];

            return (
                <div className="w-64 h-screen border-r border-slate-100 flex flex-col fixed left-0 top-0 bg-white z-10">
                    <div className="p-6 flex items-center space-x-3 mb-8">
                        <div className="w-10 h-10 bg-black rounded-lg flex items-center justify-center text-white">
                            <i className="ph-fill ph-handbag text-2xl"></i>
                        </div>
                        <div>
                            <h1 className="font-black text-lg leading-tight tracking-tight">LUXESTORE</h1>
                            <p className="text-[9px] font-bold text-slate-400 uppercase tracking-widest">Premium Goods</p>
                        </div>
                    </div>
                    <nav className="flex-1 px-4 space-y-2">
                        {tabs.map(tab => (
                            <button key={tab.id} onClick={() => setActiveTab(tab.id)}
                                className={`w-full flex items-center justify-between px-4 py-3 rounded-lg text-sm font-semibold transition-colors ${activeTab === tab.id ? 'bg-slate-50 text-black' : 'text-slate-500 hover:text-black hover:bg-slate-50'}`}>
                                <div className="flex items-center space-x-3">
                                    <i className={`ph ph-${tab.icon} text-xl`}></i>
                                    <span>{tab.name}</span>
                                </div>
                                {tab.badge > 0 && <span className="bg-black text-white text-[10px] w-5 h-5 flex items-center justify-center rounded-full">{tab.badge}</span>}
                            </button>
                        ))}
                    </nav>
                    <div className="p-6 bg-slate-50 mt-auto border-t border-slate-100 flex items-center space-x-3">
                        <div className="w-10 h-10 bg-black rounded-full text-white flex items-center justify-center font-bold text-sm">AC</div>
                        <div>
                            <p className="text-sm font-bold">Alex Carter</p>
                            <p className="text-[10px] text-slate-500 font-semibold">Premium Member</p>
                        </div>
                    </div>
                </div>
            );
        };

        const TopBar = () => (
            <header className="h-20 border-b border-slate-100 flex items-center justify-between px-10 sticky top-0 bg-white/80 backdrop-blur-md z-10 ml-64">
                <div className="relative w-96">
                    <i className="ph ph-magnifying-glass absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 text-lg"></i>
                    <input type="text" placeholder="Search for products, brands..." className="w-full bg-slate-50 border-none rounded-full py-2.5 pl-12 pr-4 text-sm focus:outline-none focus:ring-2 focus:ring-slate-200" />
                </div>
                <div className="flex items-center space-x-6 text-slate-500">
                    <button className="hover:text-black transition-colors"><i className="ph ph-heart text-2xl"></i></button>
                    <button className="hover:text-black transition-colors"><i className="ph ph-bell text-2xl"></i></button>
                </div>
            </header>
        );

        const ShopCatalog = ({ products, addToCart }) => (
            <div className="p-10 ml-64">
                <div className="flex justify-between items-end mb-8">
                    <div>
                        <h2 className="text-2xl font-bold mb-1">New Arrivals</h2>
                        <p className="text-sm text-slate-500">Discover the latest premium tech and lifestyle products.</p>
                    </div>
                    <div className="flex items-center space-x-2 border border-slate-200 rounded-lg px-3 py-1.5 text-sm font-medium">
                        <span className="text-slate-500">Sort by:</span>
                        <select className="bg-transparent font-semibold focus:outline-none cursor-pointer">
                            <option>Featured</option>
                            <option>Price: Low to High</option>
                            <option>Price: High to Low</option>
                        </select>
                    </div>
                </div>
                
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    {products.map(p => (
                        <div key={p.id} className="group cursor-pointer">
                            <div className="relative rounded-2xl overflow-hidden mb-4 bg-slate-50 aspect-square flex items-center justify-center">
                                <img src={p.image_url} alt={p.name} className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-500" />
                                {p.badge && (
                                    <span className={`absolute top-4 left-4 text-[10px] font-bold px-2 py-1 rounded bg-white shadow-sm ${p.badge === 'NEW' ? 'text-black' : 'text-red-500'}`}>
                                        {p.badge}
                                    </span>
                                )}
                                <button className="absolute top-4 right-4 w-8 h-8 bg-white rounded-full flex items-center justify-center shadow-sm text-slate-400 hover:text-red-500 transition-colors">
                                    <i className="ph-fill ph-heart"></i>
                                </button>
                                <div className="absolute inset-x-4 bottom-4 opacity-0 group-hover:opacity-100 transition-opacity">
                                    <button onClick={(e) => { e.stopPropagation(); addToCart(p); }} className="w-full bg-black text-white font-semibold py-3 rounded-xl shadow-lg hover:bg-slate-800 transition-colors">Add to Cart</button>
                                </div>
                            </div>
                            <h3 className="font-bold text-slate-800 mb-1">{p.name}</h3>
                            <p className="text-xs text-slate-500 mb-2">{p.description}</p>
                            <div className="flex items-center space-x-2">
                                <span className="font-bold">${p.price.toFixed(2)}</span>
                                {p.original_price && <span className="text-xs text-slate-400 line-through">${p.original_price.toFixed(2)}</span>}
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        );

        const ShoppingCart = ({ cart, updateQty, removeFromCart, setActiveTab }) => {
            const subtotal = cart.reduce((acc, item) => acc + (item.price * item.qty), 0);
            const tax = subtotal * 0.08;
            const total = subtotal + tax;

            if (cart.length === 0) return (
                <div className="p-10 ml-64 flex flex-col items-center justify-center h-[calc(100vh-80px)] text-center">
                    <i className="ph ph-shopping-bag text-6xl text-slate-200 mb-4"></i>
                    <h2 className="text-2xl font-bold mb-2">Your cart is empty</h2>
                    <p className="text-slate-500 mb-6">Looks like you haven't added anything to your cart yet.</p>
                    <button onClick={() => setActiveTab('catalog')} className="bg-black text-white px-6 py-3 rounded-xl font-semibold hover:bg-slate-800">Continue Shopping</button>
                </div>
            );

            return (
                <div className="p-10 ml-64">
                    <h2 className="text-2xl font-bold mb-8">Shopping Cart ({cart.length} items)</h2>
                    <div className="flex flex-col lg:flex-row gap-10">
                        <div className="flex-1 space-y-4">
                            {cart.map(item => (
                                <div key={item.id} className="flex border border-slate-200 rounded-2xl p-4 items-center bg-white">
                                    <div className="w-24 h-24 bg-slate-50 rounded-xl overflow-hidden flex-shrink-0">
                                        <img src={item.image_url} alt={item.name} className="w-full h-full object-cover" />
                                    </div>
                                    <div className="ml-6 flex-1">
                                        <h3 className="font-bold text-lg">{item.name}</h3>
                                        <p className="text-xs text-slate-500 mb-4">Color: {item.id === 1 ? 'Matte Black' : 'White'}</p>
                                        <div className="flex items-center space-x-4">
                                            <div className="flex items-center border border-slate-200 rounded-lg overflow-hidden">
                                                <button onClick={() => updateQty(item.id, -1)} className="px-3 py-1 text-slate-500 hover:bg-slate-50 transition-colors">-</button>
                                                <span className="px-3 py-1 text-sm font-semibold border-x border-slate-200">{item.qty}</span>
                                                <button onClick={() => updateQty(item.id, 1)} className="px-3 py-1 text-slate-500 hover:bg-slate-50 transition-colors">+</button>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="text-right flex flex-col justify-between h-24">
                                        <button onClick={() => removeFromCart(item.id)} className="text-slate-300 hover:text-red-500 transition-colors ml-auto"><i className="ph-fill ph-trash text-lg"></i></button>
                                        <div className="font-bold text-lg">${(item.price * item.qty).toFixed(2)}</div>
                                    </div>
                                </div>
                            ))}
                        </div>
                        <div className="w-full lg:w-96">
                            <div className="bg-slate-50 rounded-3xl p-8 border border-slate-100">
                                <h3 className="font-bold text-lg mb-6">Order Summary</h3>
                                <div className="space-y-4 text-sm mb-6 pb-6 border-b border-slate-200">
                                    <div className="flex justify-between"><span className="text-slate-500">Subtotal</span><span className="font-semibold">${subtotal.toFixed(2)}</span></div>
                                    <div className="flex justify-between"><span className="text-slate-500">Shipping</span><span className="text-emerald-500 font-semibold">Free</span></div>
                                    <div className="flex justify-between"><span className="text-slate-500">Estimated Tax</span><span className="font-semibold">${tax.toFixed(2)}</span></div>
                                </div>
                                <div className="flex justify-between items-center mb-8">
                                    <span className="font-bold text-lg">Total</span>
                                    <span className="font-black text-2xl">${total.toFixed(2)}</span>
                                </div>
                                <button onClick={() => setActiveTab('checkout')} className="w-full bg-black text-white py-4 rounded-xl font-bold hover:bg-slate-800 transition-colors mb-4">Proceed to Checkout</button>
                                <p className="text-xs text-center text-slate-400 flex items-center justify-center"><i className="ph-fill ph-lock-key mr-1"></i> Secure Encrypted Checkout</p>
                            </div>
                        </div>
                    </div>
                </div>
            );
        };

        const Checkout = ({ cart }) => {
            const subtotal = cart.reduce((acc, item) => acc + (item.price * item.qty), 0);
            const total = subtotal + (subtotal * 0.08);

            return (
                <div className="p-10 ml-64 max-w-5xl mx-auto">
                    <button className="flex items-center text-slate-500 hover:text-black font-semibold mb-8 transition-colors"><i className="ph ph-arrow-left mr-2"></i> Secure Checkout</button>
                    <div className="flex flex-col lg:flex-row gap-12">
                        <div className="flex-1 space-y-8">
                            <section>
                                <h3 className="font-bold text-lg mb-4 flex items-center"><i className="ph-fill ph-map-pin text-black mr-2"></i> 1. Shipping Address</h3>
                                <div className="border border-black rounded-xl p-5 relative bg-white">
                                    <div className="absolute top-4 right-4 text-black"><i className="ph-fill ph-check-circle text-xl"></i></div>
                                    <h4 className="font-bold mb-1">Alex Carter</h4>
                                    <p className="text-sm text-slate-500 leading-relaxed">123 Innovation Drive, Suite 400<br/>San Francisco, CA 94105<br/>+1 (555) 123-4567</p>
                                </div>
                                <button className="mt-4 text-sm font-semibold text-slate-500 flex items-center hover:text-black transition-colors"><i className="ph ph-plus mr-1"></i> Add New Address</button>
                            </section>
                            
                            <section>
                                <h3 className="font-bold text-lg mb-4 flex items-center"><i className="ph-fill ph-credit-card text-black mr-2"></i> 2. Payment Method</h3>
                                <div className="border border-slate-200 rounded-2xl p-6 bg-white space-y-6">
                                    <div className="space-y-3">
                                        <label className="flex items-center justify-between border border-slate-200 rounded-xl p-4 cursor-pointer hover:border-black transition-colors bg-slate-50">
                                            <div className="flex items-center space-x-3">
                                                <input type="radio" name="payment" defaultChecked />
                                                <div><p className="font-bold text-sm">Credit Card ends in &bull;&bull;&bull;&bull; 4242</p><p className="text-[10px] text-slate-500">Exp: 12/25</p></div>
                                            </div>
                                            <i className="ph-fill ph-credit-card text-blue-600 text-2xl"></i>
                                        </label>
                                        <label className="flex items-center justify-between border border-slate-100 rounded-xl p-4 cursor-pointer hover:border-black transition-colors">
                                            <div className="flex items-center space-x-3">
                                                <input type="radio" name="payment" />
                                                <p className="font-bold text-sm">PayPal</p>
                                            </div>
                                            <i className="ph-fill ph-paypal-logo text-blue-500 text-2xl"></i>
                                        </label>
                                    </div>
                                    <div className="pt-4 border-t border-slate-100 space-y-4">
                                        <div><label className="block text-xs font-bold text-slate-500 mb-1 uppercase tracking-wider">Cardholder Name</label><input type="text" defaultValue="ALEX CARTER" className="w-full border border-slate-200 rounded-lg px-4 py-2 text-sm focus:outline-none focus:border-black bg-slate-50" readOnly /></div>
                                        <div className="flex space-x-4">
                                            <div className="flex-1"><label className="block text-xs font-bold text-slate-500 mb-1 uppercase tracking-wider">Card Number</label><input type="text" defaultValue="**** **** **** 4242" className="w-full border border-slate-200 rounded-lg px-4 py-2 text-sm focus:outline-none focus:border-black bg-slate-50" readOnly /></div>
                                            <div className="w-24"><label className="block text-xs font-bold text-slate-500 mb-1 uppercase tracking-wider">CVV</label><input type="text" placeholder="•••" className="w-full border border-slate-200 rounded-lg px-4 py-2 text-sm focus:outline-none focus:border-black" /></div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        <div className="w-full lg:w-80">
                            <div className="bg-black text-white rounded-2xl p-8 shadow-2xl sticky top-28">
                                <h3 className="font-bold mb-6">Pay Now</h3>
                                <div className="flex justify-between items-center mb-8 border-b border-slate-800 pb-6">
                                    <span className="text-sm text-slate-400">Total Amount</span>
                                    <span className="font-black text-2xl">${total.toFixed(2)}</span>
                                </div>
                                <button className="w-full bg-white text-black py-4 rounded-xl font-bold flex items-center justify-center space-x-2 hover:bg-slate-200 transition-colors mb-4">
                                    <span>Place Order</span> <i className="ph ph-arrow-right"></i>
                                </button>
                                <p className="text-[9px] text-center text-slate-500">By placing this order, you agree to our Terms of Service and Privacy Policy</p>
                            </div>
                        </div>
                    </div>
                </div>
            );
        };

        const Profile = () => (
            <div className="p-10 ml-64 max-w-5xl">
                <h2 className="text-2xl font-bold mb-8">My Profile</h2>
                <div className="flex flex-col lg:flex-row gap-8">
                    <div className="w-full lg:w-72">
                        <div className="border border-slate-200 rounded-3xl p-8 flex flex-col items-center text-center bg-white shadow-sm mb-4">
                            <div className="relative mb-4">
                                <div className="w-24 h-24 bg-black rounded-full text-white flex items-center justify-center font-bold text-3xl">AC</div>
                                <button className="absolute bottom-0 right-0 w-8 h-8 bg-white border border-slate-200 rounded-full flex items-center justify-center text-black hover:bg-slate-50"><i className="ph-fill ph-camera"></i></button>
                            </div>
                            <h3 className="font-bold text-xl">Alex Carter</h3>
                            <p className="text-xs text-slate-500 font-semibold mb-6">Premium Member</p>
                            <div className="w-full space-y-2">
                                <button className="w-full flex items-center px-4 py-2.5 bg-slate-50 text-black font-semibold rounded-lg text-sm"><i className="ph ph-user mr-3 text-lg"></i> Account Details</button>
                                <button className="w-full flex items-center px-4 py-2.5 text-slate-500 hover:bg-slate-50 font-semibold rounded-lg text-sm transition-colors"><i className="ph ph-receipt mr-3 text-lg"></i> Order History</button>
                                <button className="w-full flex items-center px-4 py-2.5 text-slate-500 hover:bg-slate-50 font-semibold rounded-lg text-sm transition-colors"><i className="ph ph-heart mr-3 text-lg"></i> Wishlist</button>
                            </div>
                        </div>
                    </div>
                    <div className="flex-1">
                        <div className="border border-slate-200 rounded-3xl p-10 bg-white shadow-sm">
                            <h3 className="font-bold text-lg mb-6 border-b border-slate-100 pb-4">Account Information</h3>
                            <div className="grid grid-cols-2 gap-6 mb-8">
                                <div><label className="block text-xs font-bold text-slate-500 mb-2 uppercase tracking-wide">First Name</label><input type="text" defaultValue="Alex" className="w-full border border-slate-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-black" /></div>
                                <div><label className="block text-xs font-bold text-slate-500 mb-2 uppercase tracking-wide">Last Name</label><input type="text" defaultValue="Carter" className="w-full border border-slate-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-black" /></div>
                            </div>
                            <div className="mb-10">
                                <label className="block text-xs font-bold text-slate-500 mb-2 uppercase tracking-wide">Email Address</label>
                                <input type="email" defaultValue="alex.carter@example.com" className="w-full border border-slate-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-black" />
                            </div>

                            <h3 className="font-bold text-lg mb-6 border-b border-slate-100 pb-4">Security</h3>
                            <div className="space-y-4 mb-8">
                                <div className="flex items-center justify-between border border-slate-100 rounded-xl p-4 bg-slate-50">
                                    <div><p className="font-bold text-sm">Password</p><p className="text-[10px] text-slate-500">Last changed 3 months ago</p></div>
                                    <button className="px-4 py-1.5 bg-white border border-slate-200 rounded-lg text-xs font-bold hover:bg-slate-100 transition-colors">Change</button>
                                </div>
                                <div className="flex items-center justify-between border border-slate-100 rounded-xl p-4 bg-slate-50">
                                    <div><p className="font-bold text-sm">Two-Factor Authentication</p><p className="text-[10px] text-slate-500">Add an extra layer of security</p></div>
                                    <div className="w-10 h-5 bg-emerald-500 rounded-full relative cursor-pointer"><div className="w-4 h-4 bg-white rounded-full absolute top-0.5 right-0.5 shadow-sm"></div></div>
                                </div>
                            </div>
                            <div className="flex justify-end"><button className="bg-black text-white px-8 py-3 rounded-xl font-bold hover:bg-slate-800 transition-colors">Save Changes</button></div>
                        </div>
                    </div>
                </div>
            </div>
        );

        const InventoryAdmin = ({ products }) => (
            <div className="p-10 ml-64">
                <div className="flex justify-between items-center mb-8">
                    <h2 className="text-2xl font-bold">Inventory Management</h2>
                    <button className="bg-black text-white px-5 py-2.5 rounded-xl font-bold text-sm flex items-center shadow-md hover:bg-slate-800 transition-colors"><i className="ph ph-plus mr-2"></i> Add Product</button>
                </div>
                <div className="bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-sm">
                    <div className="p-4 border-b border-slate-100 flex justify-between items-center bg-slate-50/50">
                        <div className="relative w-64">
                            <i className="ph ph-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
                            <input type="text" placeholder="Search SKU or Name..." className="w-full bg-white border border-slate-200 rounded-lg py-1.5 pl-9 pr-3 text-xs focus:outline-none focus:border-black" />
                        </div>
                        <div className="flex space-x-3">
                            <select className="border border-slate-200 rounded-lg px-3 py-1.5 text-xs font-semibold focus:outline-none"><option>All Categories</option></select>
                            <select className="border border-slate-200 rounded-lg px-3 py-1.5 text-xs font-semibold focus:outline-none"><option>Status: All</option></select>
                        </div>
                    </div>
                    <table className="w-full text-left border-collapse">
                        <thead>
                            <tr className="text-[10px] text-slate-400 uppercase tracking-widest border-b border-slate-100">
                                <th className="px-6 py-4 font-bold">Product</th>
                                <th className="px-6 py-4 font-bold">SKU</th>
                                <th className="px-6 py-4 font-bold">Price</th>
                                <th className="px-6 py-4 font-bold">Stock</th>
                                <th className="px-6 py-4 font-bold">Status</th>
                                <th className="px-6 py-4 font-bold text-right">Actions</th>
                            </tr>
                        </thead>
                        <tbody className="text-sm">
                            {products.map(p => (
                                <tr key={p.id} className="border-b border-slate-50 hover:bg-slate-50 transition-colors">
                                    <td className="px-6 py-4 flex items-center space-x-4">
                                        <div className="w-10 h-10 bg-slate-100 rounded overflow-hidden"><img src={p.image_url} className="w-full h-full object-cover"/></div>
                                        <span className="font-bold text-slate-800">{p.name}</span>
                                    </td>
                                    <td className="px-6 py-4 text-slate-400 text-xs tracking-wider">{p.sku}</td>
                                    <td className="px-6 py-4 font-semibold">${p.price.toFixed(2)}</td>
                                    <td className="px-6 py-4 font-semibold"><span className={p.stock < 10 && p.stock > 0 ? "text-red-500" : (p.stock === 0 ? "text-slate-300" : "text-slate-700")}>{p.stock} units</span></td>
                                    <td className="px-6 py-4">
                                        <span className={`text-[10px] font-bold px-2 py-1 rounded ${p.status === 'In Stock' ? 'bg-emerald-50 text-emerald-600' : (p.status === 'Low Stock' ? 'bg-red-50 text-red-600' : 'bg-slate-100 text-slate-500')}`}>{p.status}</span>
                                    </td>
                                    <td className="px-6 py-4 text-right text-slate-400 text-lg space-x-2">
                                        <button className="hover:text-black transition-colors"><i className="ph-fill ph-pencil-simple"></i></button>
                                        <button className="hover:text-red-500 transition-colors"><i className="ph-fill ph-trash"></i></button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        );

        // --- MAIN APP COMPONENT --- //
        const App = () => {
            const [activeTab, setActiveTab] = useState('catalog');
            const [products, setProducts] = useState([]);
            const [cart, setCart] = useState([]);

            useEffect(() => {
                fetch('/api/products').then(r => r.json()).then(data => setProducts(data));
            }, []);

            const addToCart = (product) => {
                setCart(prev => {
                    const existing = prev.find(i => i.id === product.id);
                    if (existing) return prev.map(i => i.id === product.id ? { ...i, qty: i.qty + 1 } : i);
                    return [...prev, { ...product, qty: 1 }];
                });
            };

            const updateQty = (id, delta) => {
                setCart(prev => prev.map(i => {
                    if (i.id === id) {
                        const newQty = i.qty + delta;
                        return newQty > 0 ? { ...i, qty: newQty } : i;
                    }
                    return i;
                }));
            };

            const removeFromCart = (id) => setCart(prev => prev.filter(i => i.id !== id));

            return (
                <div className="flex min-h-screen">
                    <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} cartCount={cart.reduce((a,c)=>a+c.qty,0)} />
                    <div className="flex-1">
                        <TopBar />
                        <main>
                            {activeTab === 'catalog' && <ShopCatalog products={products} addToCart={addToCart} />}
                            {activeTab === 'cart' && <ShoppingCart cart={cart} updateQty={updateQty} removeFromCart={removeFromCart} setActiveTab={setActiveTab} />}
                            {activeTab === 'checkout' && <Checkout cart={cart} />}
                            {activeTab === 'profile' && <Profile />}
                            {activeTab === 'admin' && <InventoryAdmin products={products} />}
                        </main>
                    </div>
                </div>
            );
        };

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
</body>
</html>"""

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
