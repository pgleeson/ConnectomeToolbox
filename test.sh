set -ex

ruff format cect/*.py cect/*/*.py
ruff check cect/*.py cect/*/*.py

pip install .[docs]


quick_test=0

if [[ ($# -eq 1) && ($1 == '-q') ]]; then
    quick_test=1
elif [[ ($# -eq 1) && ($1 == '-qq') ]]; then
    quick_test=2
else
    mv docs/*data*md /tmp  2>/dev/null || true
    mv docs/assets/*json /tmp  2>/dev/null || true
fi

##   Test readers
                                                                                                                    
python -m cect.Cells $quick_test

if [ "$quick_test" == 0 ]; then

    python -m pytest -vs

    python -m cect.readers.TestDataReader -nogui                                                                                                                                         
    python -m cect.ConnectomeView                                                                                                                             
    python -m cect.ConnectomeDataset -nogui

    # Note: all run when Cells above called...
    
    #python -m cect.readers.Cook2019DataReader
    #python -m cect.readers.Cook2019HermReader -nogui
    #python -m cect.readers.WormNeuroAtlasReader -nogui
    #python -m cect.readers.WitvlietDataReader1
    #python -m cect.readers.WitvlietDataReader2
    python -m cect.readers.WhiteDataReader
    python -m cect.Analysis -nogui
    #python -m cect.readers.White_A
    #python -m cect.readers.White_L4

    #python -m cect.Comparison 0
    
    #mkdocs build
fi


echo
echo "  Successfully completed all cect tests (quick run: $quick_test)!"
echo
  

