#!/bin/bash

rm -f ${{ env.GENERATED_CODE_LOCATION }}/${{ env.CONFIG_VARIABLES_TARGET_FILE_NAME }}
touch ${{ env.GENERATED_CODE_LOCATION }}/${{ env.CONFIG_VARIABLES_TARGET_FILE_NAME }}
cat ${{ env.CONFIG_VARIABLES_FOLDER }}/members.yml ${{ env.CONFIG_VARIABLES_FOLDER }}/teams.yml ${{ env.CONFIG_VARIABLES_FOLDER }}/github.yml ${{ env.CONFIG_VARIABLES_FOLDER }}/datadog.yml ${{ env.CONFIG_VARIABLES_FOLDER }}/discord.yml ${{ env.CONFIG_VARIABLES_FOLDER }}/terraformCloud.yml > ${{ env.GENERATED_CODE_LOCATION }}/${{ env.CONFIG_VARIABLES_TARGET_FILE_NAME }}
