from azure.datalake.store import core, lib, multithread
token = lib.auth(tenant_id, username, password)
adl = core.AzureDLFileSystem(token, store_name=store_name)

# typical operations
adl.ls('')
adl.ls('tmp/', detail=True)
adl.ls('tmp/', detail=True, invalidate_cache=True)
adl.cat('samplefile')
adl.head('example.csv')

# file-like object
with adl.open('example.csv', blocksize=2**20) as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
    # could have passed f to any function requiring a file object:
    # pandas.read_csv(f)

with adl.open('far_and_beyond', 'wb') as f:
    # data is written on flush/close, or when buffer is bigger than
    # blocksize
    f.write(b'important data')

adl.du('far_and_beyond')

multithread.ADLDownloader(adl, "", 'tmp/', 5, 2**24)