#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
    printf("Escalate permission from %d to root\n", getuid());
    setuid(0);
    printf("Execute rtcwake with uid: %d\n", getuid());
    system("rtcwake -m freeze -s 1");
    printf("Done\n");
    return 0;
}
