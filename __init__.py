import pandas as pd

keywords_df = pd.DataFrame(columns=['Ad Group', 'Keyword', 'Campaign', 'Criterion Type']);

products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']
words = ['buy', 'prices', 'offer', 'discount', 'save', 'promotion', 'rebate']
match_types = ['Exact']

for product in products:
    for word in words:

        # generate keywords
        keyword = product.lower() + ' ' + word

        row = {
            'Ad Group': product,
            'Keyword': keyword,
            'Campaign': 'SEM_Sofas',
            'Criterion Type': match_types[0]
        }

        keywords_df.loc[len(keywords_df)] = row  # store it into the new dataframe

# do the same by having the keywords come before the products name
for product in products:
    for word in words:

        keyword = word + ' ' + product.lower() 

        row = {
            'Ad Group': product,
            'Keyword': keyword,
            'Campaign': 'SEM_Sofas',
            'Criterion Type': match_types[0]
        }

        keywords_df.loc[len(keywords_df)] = row  # store it into the new dataframe

# print new dataframe
print(keywords_df)

# export the dataframe to csv file
keywords_df.to_csv('keywords.csv')
