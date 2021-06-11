foo = input()
print(f'stdout: {foo}')
raise RuntimeError(f'stderr: {foo}')
