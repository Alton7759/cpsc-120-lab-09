#!/bin/bash

LABNUM="09"
LAB="cpsc-120-lab-${LABNUM}"
GRADING_LOG="grading_log.csv"

MAXJOBS=5
MAKEJOBS=3

COPYACTIONS="NO"
# Just in case you need to copy the actions or an updated solution_check.py
ACTIONHOME="${HOME}/github/teaching-ci/actions"
if [ "${COPYACTIONS}X" = "YESX" ]; then
    for i in *-${LAB}-*; do
        cp ${ACTIONHOME}/*.py ${i}/.action
    done
fi

COPYMAKEFILES="NO"
# Just in case you need to copy Makefiles or something else
REPOHOME="${HOME}/github/cpsc120/cpsc-120-solution-lab-${LABNUM}
if [ "${COPYMAKEFILES}X" = "YESX" ]; then
    for repo in *-${LAB}-*; do
        cp ${REPOHOME}/Makefile ${repo}
        i=1
        while [ $i -lt 10 ]; do
            if [ ! -d ${repo}/part-${i} ]; then
                break
            else
                cp ${REPOHOME}/part-${i}/Makefile ${repo}/part-${i}
            fi
            i=$((i+1))
        done
    done
fi



for i in *-${LAB}-*; do
    pushd $i >& /dev/null
    nohup make -j ${MAKEJOBS} test >& make_test_log.txt &
    popd
    N=$(jobs -p | wc -l)
    while [ $N -gt $MAXJOBS ]; do
        echo "Sleeping for a second"
        sleep 1
        N=$(jobs -p | wc -l)
    done
done

# Get the headers
head -1 `ls */.*${LAB}*_part-*gradelog.csv | head -1` > ${GRADING_LOG}
# Collect the rows
for i in *-${LAB}-*; do
    tail -q -n +2 ${i}/.*${LAB}*_part-*gradelog.csv >> ${GRADING_LOG};
done
