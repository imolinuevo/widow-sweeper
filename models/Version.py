class Version(object):

    def __init__(self):
        self.major = 0
        self.minor = 0
        self.build = 1

    def __str__(self):
        string = """

                      .                      .-.
..-.     .-.  .-.     /                 .--.-'
   )   (     `-'.-../ .-._.`)    (    (  (_)`)    (   .-.   .-. .-.   .-.  ).--.
  /     \   /  (   / (   ) /  .   )    `-.  /  .   )./.-'_./.-'_/  )./.-'_/
 (   .   ).(__. `-'-..`-' (_.' `-'   _    )(_.' `-' (__.' (__.'/`-' (__.'/
  `-' `-'                           (_.--'                    /

        """
        return string + "\nWidow Sweeper v" + str(self.major) + "." + str(self.minor) + "." + str(self.build)
