def displayInventory(inventory):
    print('inventory:')
    item_total = 0
    for k, v in inventory.items():
        #fill here
        print(v, k)
        try:
            item_total = item_total+int(v)
        except:
            print('error occur at int cast')
            break

    print('total num of items: ' + str(item_total))


def addToInventory(inventory, addedItems):
    #code
    #print(type(addedItems))
    for item in addedItems:
        inventory.setdefault(item, 0)
        
        #add the item count
        inventory[item]+=1
        #print(inventory[item])
    
    return inventory


if __name__ == '__main__':
    
    stuff = {'rope': 1, 'torch': '6', 'gold coin': 42, 'dagger': 1, 'arrow': 12}

    #displayInventory(stuff)

    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)


