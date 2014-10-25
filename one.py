
##############################################################################
#
#       OOOOOOOOO     NNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEE
#     OO:::::::::OO   N:::::::N       N::::::NE::::::::::::::::::::E
#   OO:::::::::::::OO N::::::::N      N::::::NE::::::::::::::::::::E
#  O:::::::OOO:::::::ON:::::::::N     N::::::NEE::::::EEEEEEEEE::::E
#  O::::::O   O::::::ON::::::::::N    N::::::N  E:::::E       EEEEEE
#  O:::::O     O:::::ON:::::::::::N   N::::::N  E:::::E             
#  O:::::O     O:::::ON:::::::N::::N  N::::::N  E::::::EEEEEEEEEE   
#  O:::::O     O:::::ON::::::N N::::N N::::::N  E:::::::::::::::E   
#  O:::::O     O:::::ON::::::N  N::::N:::::::N  E:::::::::::::::E   
#  O:::::O     O:::::ON::::::N   N:::::::::::N  E::::::EEEEEEEEEE   
#  O:::::O     O:::::ON::::::N    N::::::::::N  E:::::E             
#  O::::::O   O::::::ON::::::N     N:::::::::N  E:::::E       EEEEEE
#  O:::::::OOO:::::::ON::::::N      N::::::::NEE::::::EEEEEEEE:::::E
#   OO:::::::::::::OO N::::::N       N:::::::NE::::::::::::::::::::E
#     OO:::::::::OO   N::::::N        N::::::NE::::::::::::::::::::E
#       OOOOOOOOO     NNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEE
#
##############################################################################

import upload, download, delete, user, argparse, signal, sys, logger, diff, requests, sys
import list as lister


SILENT = False


def build_arg_parser():
  # Create Arg parser
  parser = argparse.ArgumentParser(description='Push and pull files from Mediafire',
      prog='One')

  parser.add_argument('sub_command', 
      help='Choose the subcommand to execute',
      choices=['push', 'pull', 'del', 'init', 'list', 'diff'], 
      type=str)
  
  parser.add_argument('files', type=str, nargs='*', help='Files to work with')

  parser.add_argument('-s', '--silent', action='store_true', help='Stop all output to stdout')

  return parser 
def main():
  parser = build_arg_parser()

  args = parser.parse_args()
  if (args.sub_command == 'push'):
    if (len(args.files) == 0):
      logger.die('Must include at least one file')
    else:
      for f in args.files:
        upload.upload(f) 
  elif (args.sub_command == 'pull'):
    if (len(args.files) == 0):
      logger.die('Must include at least one file')
    else:
      for f in args.files:
        download.download(f)
  elif (args.sub_command == 'del'):
    if (len(args.files) == 0):
      logger.die('Must include at least one file')
    else:
      for f in args.files:
          delete.delete(f)
  elif (args.sub_command == 'init'):
    if (user.is_user_signed_in()):
      logger.end('User is already initialized')
    else:
      user.get_auth()
  elif (args.sub_command == 'list'):
    lister.list_files()
  elif (args.sub_command == 'diff'):
    if (len(args.files) == 0):
      logger.die('Must include at least one file')
    else:
      for f in args.files:
        diff.diff(f)

if __name__ == '__main__':
  def sigint_handler(signal, frame):
    sys.stdout.write('\nCaught Control-C. Exiting now.\n')
    sys.exit(130)
  signal.signal(signal.SIGINT, sigint_handler)
  main() 
