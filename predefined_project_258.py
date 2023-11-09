#Predefined code begins
from tkinter import *
from tkinter import messagebox
from web3 import Web3
from PIL import ImageTk, Image
root = Tk()
root.title("My Crypto Banking App")
root.configure(background="white")
ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))
img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
panel = Label(root, image=img, bg='white')
panel.pack(side="top")
#Predefined code stops

#create a frame, Labels and entry element and place them on the frame







frame=Frame(
    root
    bg='white'
    padx=5
    pady=5)




def openNewWindow():
    #get the username and password and check with a predefined username and password and create a new window
   
    account1.grid(row=0, column=1, pady=10, padx=20)
    account2.grid(row=1, column=1, pady=10, padx=20)

   
        
       

    
        #Predefined code begins
        right_frame = Frame(
            newWindow,
            bd=2,
            bg='white',
            padx=10,
            pady=10
        )
        Label(
            right_frame,
            text="Account number 1:",
            fg='black',
            bg='white',
        ).grid(row=0, column=0, sticky=W, pady=10)
        Label(
            right_frame,
            text="Account number 2:",
            fg='black',
            bg='white',
        ).grid(row=1, column=0, sticky=W, pady=10)
        Label(
            right_frame,
            text="Private Key:",
            fg='black',
            bg='white',
        ).grid(row=2, column=0, sticky=W, pady=10)
        Label(
            right_frame,
            text="ETH:",
            fg='black',
            bg='white',
        ).grid(row=3, column=0, sticky=W, pady=10)
        Label(
            right_frame,
            text="Gas Price (GWEI):",
            fg='black',
            bg='white',
        ).grid(row=4, column=0, sticky=W, pady=10)
        Label(
            right_frame,
            text="Gas Limit:",
            fg='black',
            bg='white',
        ).grid(row=5, column=0, sticky=W, pady=10)
        account1 = Entry(
            right_frame,
        )
        account2 = Entry(
            right_frame,
        )
        private_key = Entry(
            right_frame,
        )
        amount = Entry(
            right_frame,
        )
        gas_price = Entry(
            right_frame,
        )
        gas_Limit = Entry(
            right_frame,
        )
        account1.grid(row=0, column=1, pady=10, padx=20)
        account2.grid(row=1, column=1, pady=10, padx=20)
        private_key.grid(row=2, column=1, pady=10, padx=20)
        amount.grid(row=3, column=1, pady=10, padx=20)
        gas_price.grid(row=4, column=1, pady=10, padx=20)
        gas_Limit.grid(row=5, column=1, pady=10, padx=20)
        def sendETH():
            account1_id = account1.get()
            account2_id = account2.get()
            eth_amount = amount.get()
            key = private_key.get()
            gas_fee = gas_price.get()
            Glimit = gas_Limit.get()
            nonce = web3.eth.getTransactionCount(account1_id)
            tx = {
                'nonce': nonce,
                'to': account2_id,
                'value': web3.toWei(eth_amount, 'ether'),
                'gas': int(Glimit),
                'gasPrice': web3.toWei(gas_fee, 'gwei')
            }
            singed_tx = web3.eth.account.signTransaction(tx, key)
            tx_hash = web3.eth.sendRawTransaction(singed_tx.rawTransaction)
            print('You transaction is successful. Your Transaction ID is:', tx_hash.hex())
            messagebox.showinfo('Transaction status!', 'Transaction Successful! Verify your metamask wallet !')
        register_btn = Button(
            right_frame,
            width=15,
            text='TRANSFERRING ETH',
            command=sendETH
        )
        register_btn.grid(row=8, column=1)
        right_frame.pack()
    else:
        messagebox.showerror('Login Status', 'invalid email or password')
        #Predefined code ends

#create a button element to call the openNewWindow function and place it on the frame.
transfer.eth=Button(root,text'TRANSFER ETH', command=sendETH,bightlgtbackground='white',width=15)


left_frame.pack()
root.mainloop()