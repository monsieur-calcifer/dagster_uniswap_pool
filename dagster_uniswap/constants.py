from dagster import file_relative_path, get_dagster_logger

TICK_BASE = 1.0001

WETH_SPX_ADDRESS = '0x00Ed26e794b949E18B142F9108429b74CE08aC99'.lower()
WETH_USDT_ADDRESS = '0x11b815efB8f581194ae79006d24E0d814B7697F6'.lower()

UNISWAP_ENDPOINT = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'

START_BLOCK = 17952250
END_BLOCK = START_BLOCK + 1000
# END_BLOCK = 18376030

TOPIC_SWAP = (
    '0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67'
)
TOPIC_BURN = (
    '0x0c396cd989a39f4459b5fa1aed6a9a8dcdbc45908acfd67e028cd568da98982c'
)
TOPIC_MINT = (
    '0x7a53080ba414158be7ec69b987b5fb7d07dee101fe85488f0853ae16239d0bde'
)
TOPIC_COLLECT = (
    '0x70935338e69775456a85ddef226c395fb668b63fa0115f5f20610b388e6ca9c0'
)
TOPIC_FLASH = (
    '0xbdbdb71d7860376ba52b25a5028beea23581364a40522f6bcfb86bb1f2dca633'
)

DIRECTORY_PATH = ''  # fill with own