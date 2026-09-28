echo "Preprocessing Riedel-NYT 2010 Dataset..."

echo "Making bags: python ./preproc/make_bags.py -data riedel"
python ./preproc/make_bags.py -data gids

echo "Generating pickle File: python ./preproc/generate_pickle.py -data riedel"
python ./preproc/generate_pickle.py -data gids