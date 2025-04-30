import pandas as pd
exports = {'International':['Cocao Butter', 'Cake', 'Liquor'],
           'Local':['Cocoa Powder', '', '']}
segments = {'Refreshment Beverages':['Bournvita', 'Hot Chocolate', '', ''],
            'Confectionary':['Tom Tom', 'Buttermint', '', ''],
            'Intermediate Cocoa Products':['Cocoa Powder', 'Cocoa Liquor', 'Cocoa Butter', 'Cocoa Cake']}
brands = {'Refreshment Beverages':['Cadbury Bournvita', 'Cadbury 3-in-1 Hot Chocolate', ''],
          'Confectionery':['TomTom Classic', 'TomTom Strawberry', 'Buttermint'],
          'Intermediate Cocoa Products':['Cocoa Powder', 'Cocoa Butter', '']}

df_exports = pd.DataFrame(exports)
df_segments = pd.DataFrame(segments)
df_brands = pd.DataFrame(brands)


with open('cadbury_market.csv', 'w', encoding='utf-8') as f:
    f.write("EXPORT PRODUCTS\n")
    df_exports.to_csv(f, index=False)
    f.write("\nSEGMENTS\n")
    df_segments.to_csv(f, index=False)
    f.write("\nBRANDS\n")
    df_brands.to_csv(f, index=False)
