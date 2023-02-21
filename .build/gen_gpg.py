import gnupg
import tempfile
import yaml
import glob
import sys

from argparse import ArgumentParser

def parse_args(args):
    usage = """
          gen_gpg.py yamlfile keyring [-d dir]
          Get GPG keys from CMS yaml file and create a GPG keyring with all listed keys
          """
    parser = ArgumentParser(usage=usage)
    parser.add_argument("yamlfile", help="YAML file with list of GPG keys to extract")
    parser.add_argument("keyring", help="output GPG keyring file")
    parser.add_argument("-d", dest="gpg_dir", help="GPG directory")
    opts = parser.parse_args(args)
    return opts

if __name__ == "__main__":
  opts = parse_args(sys.argv[1:])

  with open(opts.yamlfile, 'r') as f:
    y=yaml.safe_load(f)
  
  fps = [ x['fingerprint'] for x in y['gpg_keys']['current'] ]
  
  with tempfile.TemporaryDirectory() as workdir:
    gpg = gnupg.GPG(gnupghome=workdir)
    
    if opts.gpg_dir:
      for f in glob.glob(f"{opts.gpg_dir}/RPM-GPG-KEY-*"):
        with open(f, 'r') as data:
          gpg.import_keys(data.read())
        #gpg.import_keys_file(f)
    else:
      for f in glob.glob('/usr/share/distribution-gpg-keys/fedora/RPM-GPG-KEY-*-primary'):
        with open(f, 'r') as data:
          gpg.import_keys(data.read())
        #gpg.import_keys_file(f)
      
      for f in glob.glob('/usr/share/distribution-gpg-keys/epel/RPM-GPG-KEY-*'):
        with open(f, 'r') as data:
          gpg.import_keys(data.read())
        #gpg.import_keys_file(f)
    
    with open(opts.keyring, 'wb') as g:
       g.write(gpg.export_keys(fps, armor=False))
  
