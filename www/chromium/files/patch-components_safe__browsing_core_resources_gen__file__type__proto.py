--- components/safe_browsing/core/resources/gen_file_type_proto.py.orig	2020-11-13 06:36:41 UTC
+++ components/safe_browsing/core/resources/gen_file_type_proto.py
@@ -31,6 +31,7 @@ def PlatformTypes():
     "android": download_file_types_pb2.DownloadFileType.PLATFORM_ANDROID,
     "chromeos": download_file_types_pb2.DownloadFileType.PLATFORM_CHROME_OS,
     "linux": download_file_types_pb2.DownloadFileType.PLATFORM_LINUX,
+    "bsd": download_file_types_pb2.DownloadFileType.PLATFORM_LINUX,
     "mac": download_file_types_pb2.DownloadFileType.PLATFORM_MAC,
     "win": download_file_types_pb2.DownloadFileType.PLATFORM_WINDOWS,
   }
@@ -169,7 +170,7 @@ class DownloadFileTypeProtoGenerator(BinaryProtoGenera
                       'Outfile must have a %d for version and %s for platform.')
     parser.add_option('-t', '--type',
                       help='The platform type. One of android, chromeos, ' +
-                      'linux, mac, win')
+                      'linux, bsd, mac, win')
 
   def AddExtraCommandLineArgsForVirtualEnvRun(self, opts, command):
     if opts.type is not None:
